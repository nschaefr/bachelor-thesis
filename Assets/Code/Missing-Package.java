import static org.junit.jupiter.api.Assertions.assertNotNull;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.springframework.web.client.RestTemplate;
import org.springframework.boot.test.context.SpringBootTest;

@SpringBootTest
public class ApplicationRestTemplateTest {

    private Application application;

    @BeforeEach
    public void setUp() {
        application = new Application();
    }

    @Test
    public void testRestTemplate() throws Exception {
        RestTemplate restTemplate = application.restTemplate();
        assertNotNull(restTemplate, "RestTemplate bean should not be null");
    }
}