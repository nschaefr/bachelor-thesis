package com.example.calculator;

import static org.junit.jupiter.api.Assertions.assertEquals;
import org.junit.jupiter.api.Test;
import java.lang.reflect.Method;

public class CalculatorSubtractTest {

    @Test
    public void testSubtractPositiveNumbers() throws Exception {
        Calculator calculator = new Calculator();
        Method method = Calculator.class.getDeclaredMethod("subtract", int.class, int.class);
        method.setAccessible(true);
        int result = (int) method.invoke(calculator, 10, 5);
        assertEquals(5, result);
    }

    @Test
    public void testSubtractNegativeNumbers() throws Exception {
        Calculator calculator = new Calculator();
        Method method = Calculator.class.getDeclaredMethod("subtract", int.class, int.class);
        method.setAccessible(true);
        int result = (int) method.invoke(calculator, -10, -5);
        assertEquals(-5, result);
    }

    @Test
    public void testSubtractPositiveAndNegativeNumbers() throws Exception {
        Calculator calculator = new Calculator();
        Method method = Calculator.class.getDeclaredMethod("subtract", int.class, int.class);
        method.setAccessible(true);
        int result = (int) method.invoke(calculator, 10, -5);
        assertEquals(15, result);
    }

    @Test
    public void testSubtractNegativeAndPositiveNumbers() throws Exception {
        Calculator calculator = new Calculator();
        Method method = Calculator.class.getDeclaredMethod("subtract", int.class, int.class);
        method.setAccessible(true);
        int result = (int) method.invoke(calculator, -10, 5);
        assertEquals(-15, result);
    }

    @Test
    public void testSubtractZero() throws Exception {
        Calculator calculator = new Calculator();
        Method method = Calculator.class.getDeclaredMethod("subtract", int.class, int.class);
        method.setAccessible(true);
        int result = (int) method.invoke(calculator, 0, 0);
        assertEquals(0, result);
    }
}