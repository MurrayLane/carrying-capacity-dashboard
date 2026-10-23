package ccdash;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;

import java.io.InputStream;
import java.util.Iterator;
import java.util.Map;

import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.DynamicTest;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.TestFactory;

import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;

/**
 * Regression test against the original QUT servlet.
 *
 * baseline.json was produced by posting the default inputs for each state and
 * territory (short- and long-term presets) to the original compiled servlet
 * running in Tomcat 9. The rebuilt model must reproduce those numbers.
 */
class CarryingCapacityModelTest {

    private static final ObjectMapper MAPPER = new ObjectMapper();
    private static CarryingCapacityModel model;
    private static JsonNode baseline;

    @BeforeAll
    static void load() throws Exception {
        try (InputStream in = CarryingCapacityModelTest.class.getResourceAsStream("/model.xls")) {
            model = new CarryingCapacityModel(in);
        }
        try (InputStream in = CarryingCapacityModelTest.class.getResourceAsStream("/baseline.json")) {
            baseline = MAPPER.readTree(in);
        }
    }

    @TestFactory
    Iterator<DynamicTest> matchesOriginalServlet() {
        Iterator<Map.Entry<String, JsonNode>> cases = baseline.fields();
        return new Iterator<>() {
            public boolean hasNext() { return cases.hasNext(); }
            public DynamicTest next() {
                Map.Entry<String, JsonNode> c = cases.next();
                return DynamicTest.dynamicTest(c.getKey(), () -> check(c.getValue()));
            }
        };
    }

    private static void check(JsonNode testCase) throws Exception {
        JsonNode params = testCase.get("params");
        JsonNode expected = testCase.get("expected");
        JsonNode actual = MAPPER.readTree(model.evaluate(n -> params.has(n) ? params.get(n).asText() : null));
        assertClose("popcc", expected.get("popcc"), actual.get("popcc"));
        assertClose("excess", expected.get("excess"), actual.get("excess"));
        assertClose("requirements", expected.get("requirements"), actual.get("requirements"));
    }

    private static void assertClose(String path, JsonNode expected, JsonNode actual) {
        if (expected.isArray()) {
            assertEquals(expected.size(), actual.size(), path + " length");
            for (int i = 0; i < expected.size(); i++) {
                assertClose(path + "[" + i + "]", expected.get(i), actual.get(i));
            }
            return;
        }
        double e = expected.asDouble(), a = actual.asDouble();
        double tolerance = Math.max(0.015, Math.abs(e) * 1e-7);
        assertTrue(Math.abs(e - a) <= tolerance, path + ": expected " + e + " but was " + a);
    }

    @Test
    void rejectsMissingParameter() {
        Map<String, String> none = Map.of();
        try {
            model.evaluate(none::get);
        } catch (IllegalArgumentException expected) {
            return;
        } catch (Exception other) {
            throw new AssertionError(other);
        }
        throw new AssertionError("expected IllegalArgumentException");
    }
}
