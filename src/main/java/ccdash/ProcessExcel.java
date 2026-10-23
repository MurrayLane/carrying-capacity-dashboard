package ccdash;

import java.io.IOException;
import java.io.InputStream;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**
 * HTTP endpoint for the dashboard: the page posts the input form here and
 * receives the model's results as JSON. Mapped at /ProcessExcel in web.xml.
 */
public class ProcessExcel extends HttpServlet {

    private static final long serialVersionUID = 1L;
    private static final String MODEL_PATH = "/WEB-INF/model.xls";

    private CarryingCapacityModel model;

    @Override
    public void init() throws ServletException {
        try (InputStream in = getServletContext().getResourceAsStream(MODEL_PATH)) {
            if (in == null) {
                throw new ServletException("Model workbook not found at " + MODEL_PATH);
            }
            model = new CarryingCapacityModel(in);
        } catch (IOException e) {
            throw new ServletException("Could not read " + MODEL_PATH, e);
        }
    }

    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws IOException {
        process(request, response);
    }

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws IOException {
        process(request, response);
    }

    private void process(HttpServletRequest request, HttpServletResponse response) throws IOException {
        String json;
        try {
            json = model.evaluate(request::getParameter);
        } catch (IllegalArgumentException e) {
            response.sendError(HttpServletResponse.SC_BAD_REQUEST, e.getMessage());
            return;
        }
        response.setContentType("application/json;charset=UTF-8");
        response.setHeader("Cache-Control", "no-store");
        response.getWriter().print(json);
    }

    @Override
    public String getServletInfo() {
        return "Evaluates the carrying-capacity model";
    }
}
