# Carrying Capacity Dashboard

An interactive estimate of how many people a region of Australia can support from its own
land, given choices about diet, waste, farming, fuel, fibre, timber, infrastructure and
nature reserve. Originally built at QUT's Institute for Future Environments (2011); this
repository is the maintained rebuild.

## How it works

- `src/main/webapp/` is the web page: one JSP, jQuery UI sliders and Flot pie charts.
  Default inputs for 60 regions are in the two `default-inputs-*.csv` files.
- `src/main/webapp/WEB-INF/model.xls` is the model: an Excel workbook whose formulas do
  all the calculation.
- `src/main/java/ccdash/CarryingCapacityModel.java` writes the 24 inputs into the first
  sheet, re-evaluates every formula with Apache POI and reads the results back.
  `ProcessExcel.java` exposes that at `POST /ProcessExcel`, returning JSON.

Changing the model means editing the workbook. Inputs go in B2:B25 of the first sheet;
results are read from B76 (carrying-capacity population), C84:D89 (excess land) and
B91:E107 (land requirements). Keep those cells where they are or update the row and
column constants in `CarryingCapacityModel`.

## Build and test

Requires JDK 17+ and Maven.

```bash
mvn verify          # compiles, runs the regression test, builds target/ROOT.war
```

The regression test (`src/test/resources/baseline.json`) replays the default inputs for
every state and territory against outputs recorded from the original QUT servlet, so a
change to the Java code or the POI version is checked against the original numbers.
If you change the workbook deliberately, regenerate the baseline.

## Run

```bash
docker build -t ccdash .
docker run --rm -p 8080:8080 ccdash
# open http://localhost:8080/
```

## Deploy

GitHub Actions builds the image and publishes it to GHCR on every push to `main`
(`.github/workflows/docker-image.yml`). Server setup and update steps are in
[`deploy/README.md`](deploy/README.md).
