public class CalculatorTest {
    @BeforeEach
    public void setUp() {
        calculator = new Calculator();
    }

    @Test
    public void testAdd() {
        int a = 5;
        int b = 3;
        int expectedResult = 8;
        int result = calculator.add(a, b);
        assertEquals(expectedResult, result, "should add 2 int");
    }

    @Test
    public void testSubtract() {
        int a = 5;
        int b = 3;
        int expectedResult = 2;
        int result = calculator.subtract(a, b);
        assertEquals(expectedResult, result, "should subtract 2 int");
    }
}