package ccdash;

import java.io.ByteArrayInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.text.DecimalFormat;
import java.text.DecimalFormatSymbols;
import java.util.Locale;
import java.util.function.Function;

import org.apache.poi.ss.usermodel.Cell;
import org.apache.poi.ss.usermodel.FormulaEvaluator;
import org.apache.poi.ss.usermodel.Row;
import org.apache.poi.ss.usermodel.Sheet;
import org.apache.poi.ss.usermodel.Workbook;
import org.apache.poi.ss.usermodel.WorkbookFactory;

/**
 * Evaluates the carrying-capacity spreadsheet model.
 *
 * The model is an Excel workbook (WEB-INF/model.xls). Inputs are written into
 * column B of the first sheet (rows 2 to 25), every formula is re-evaluated,
 * and three result blocks are read back:
 *
 * <ul>
 *   <li>B76: carrying-capacity population</li>
 *   <li>C84:D89: excess land by existing use (area, share)</li>
 *   <li>B91:E107: land requirements by use (two areas, two shares)</li>
 * </ul>
 *
 * Instances are thread-safe: the workbook bytes are held in memory and a fresh
 * workbook is opened per evaluation, because POI workbooks are not thread-safe.
 */
public final class CarryingCapacityModel {

    /** Request parameter names, in the order their values are written to column B from row 2. */
    private static final String[] INPUT_ROWS = {
        "inputRegionId",
        "inputAreasCropping",
        "inputAreasPasture",
        "inputAreasNonAg",
        "inputAreasBuilt",
        "inputAreasNature",
        "inputResilienceYears",
        "inputFoodRatio",
        "inputMeateggRatio",
        "inputRedmeatRatio",
        "inputActivityLevel",
        "inputRecyclingRatio",
        "inputLossesRatio",
        "inputOrganicRatio",
        "inputIrrigationRatio",
        "inputFuelTotal",
        "inputBiofuelRatio",
        "inputFibreTotal",
        "inputFibreNaturalRatio",
        "inputFibreWoolRatio",
        "inputTimber",
        "inputInfrastructure",
        "inputNatureRatio",
        "inputPopulation",
    };

    /** Parameters entered as percentages in the UI; the model expects fractions. */
    private static final java.util.Set<String> PERCENT_INPUTS = java.util.Set.of(
        "inputFoodRatio", "inputMeateggRatio", "inputRedmeatRatio", "inputRecyclingRatio",
        "inputLossesRatio", "inputOrganicRatio", "inputIrrigationRatio", "inputBiofuelRatio",
        "inputFibreNaturalRatio", "inputFibreWoolRatio", "inputNatureRatio");

    /** Parameters the UI formats with thousands separators; digits only are kept. */
    private static final java.util.Set<String> DIGITS_ONLY_INPUTS = java.util.Set.of(
        "inputPopulation", "inputAreasCropping", "inputAreasPasture", "inputAreasNonAg",
        "inputAreasBuilt", "inputAreasNature");

    private static final int POPCC_ROW = 75;
    private static final int EXCESS_FIRST_ROW = 83, EXCESS_END_ROW = 89;
    private static final int REQ_FIRST_ROW = 90, REQ_END_ROW = 107;

    private final byte[] workbookBytes;

    public CarryingCapacityModel(InputStream workbook) throws IOException {
        this.workbookBytes = workbook.readAllBytes();
    }

    /**
     * Evaluates the model for one set of inputs.
     *
     * @param params lookup of request parameter name to raw value
     * @return a JSON object with keys popcc, excess and requirements
     * @throws IllegalArgumentException if a parameter is missing or not numeric
     */
    public String evaluate(Function<String, String> params) throws IOException {
        double[] values = new double[INPUT_ROWS.length];
        for (int i = 0; i < INPUT_ROWS.length; i++) {
            values[i] = parse(INPUT_ROWS[i], params.apply(INPUT_ROWS[i]));
        }

        DecimalFormat df = new DecimalFormat("#.##", DecimalFormatSymbols.getInstance(Locale.ROOT));
        try (Workbook wb = WorkbookFactory.create(new ByteArrayInputStream(workbookBytes))) {
            Sheet sheet = wb.getSheetAt(0);
            for (int i = 0; i < values.length; i++) {
                cell(sheet, i + 1, 1).setCellValue(values[i]);
            }
            FormulaEvaluator evaluator = wb.getCreationHelper().createFormulaEvaluator();
            evaluator.evaluateAll();

            StringBuilder json = new StringBuilder(2048);
            json.append("{ \"popcc\": ").append(df.format(num(sheet, POPCC_ROW, 1)));

            json.append("\n, \"excess\": [");
            for (int r = EXCESS_FIRST_ROW; r < EXCESS_END_ROW; r++) {
                if (r > EXCESS_FIRST_ROW) json.append(',');
                json.append('[').append(df.format(num(sheet, r, 2)))
                    .append(',').append(df.format(num(sheet, r, 3) * 100.0)).append(']');
            }
            json.append(']');

            json.append("\n, \"requirements\": [");
            for (int r = REQ_FIRST_ROW; r < REQ_END_ROW; r++) {
                if (r > REQ_FIRST_ROW) json.append(',');
                json.append('[').append(df.format(num(sheet, r, 1)))
                    .append(',').append(df.format(num(sheet, r, 2)))
                    .append(',').append(df.format(num(sheet, r, 3) * 100.0))
                    .append(',').append(df.format(num(sheet, r, 4) * 100.0)).append(']');
            }
            json.append("]\n}");
            return json.toString();
        }
    }

    private static double parse(String name, String raw) {
        if (raw == null) {
            throw new IllegalArgumentException("Missing parameter " + name);
        }
        String s = DIGITS_ONLY_INPUTS.contains(name) ? raw.replaceAll("[\\D]", "") : raw.trim();
        try {
            double v = Double.parseDouble(s);
            return PERCENT_INPUTS.contains(name) ? v / 100.0 : v;
        } catch (NumberFormatException e) {
            throw new IllegalArgumentException("Parameter " + name + " is not a number: " + raw);
        }
    }

    private static Cell cell(Sheet sheet, int rowIndex, int colIndex) {
        Row row = sheet.getRow(rowIndex);
        if (row == null) row = sheet.createRow(rowIndex);
        Cell c = row.getCell(colIndex);
        return c != null ? c : row.createCell(colIndex);
    }

    private static double num(Sheet sheet, int rowIndex, int colIndex) {
        return cell(sheet, rowIndex, colIndex).getNumericCellValue();
    }
}
