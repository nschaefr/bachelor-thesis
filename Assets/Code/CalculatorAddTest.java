package com.example.calculator;

import static org.junit.jupiter.api.Assertions.assertEquals;
import org.junit.jupiter.api.Test;

public class CalculatorAddTest {

    @Test
    public void testAddPositiveNumbers() {
        Calculator calculator = new Calculator();
        int result = calculator.add(2, 3);
        assertEquals(5, result);
    }

    @Test
    public void testAddNegativeNumbers() {
        Calculator calculator = new Calculator();
        int result = calculator.add(-2, -3);
        assertEquals(-5, result);
    }

    @Test
    public void testAddPositiveAndNegativeNumbers() {
        Calculator calculator = new Calculator();
        int result = calculator.add(2, -3);
        assertEquals(-1, result);
    }

    @Test
    public void testAddZero() {
        Calculator calculator = new Calculator();
        int result = calculator.add(0, 0);
        assertEquals(0, result);
    }

    @Test
    public void testAddPositiveNumberAndZero() {
        Calculator calculator = new Calculator();
        int result = calculator.add(5, 0);
        assertEquals(5, result);
    }

    @Test
    public void testAddNegativeNumberAndZero() {
        Calculator calculator = new Calculator();
        int result = calculator.add(-5, 0);
        assertEquals(-5, result);
    }
}