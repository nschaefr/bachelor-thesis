@Test
public void testAdd() {
    // Arrange
    Calculator calculator = new Calculator();
    int a = 5;
    int b = 3;
    int expectedResult = 8;

    // Act
    int result = calculator.add(a, b);

    // Assert
    assertEquals(expectedResult, result, "The add method should add two integers correctly");
}