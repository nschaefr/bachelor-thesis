package com.senec.emsrelay.filter;

import org.junit.jupiter.api.Test;

public class ErrorResponseFilterGetOrderTest {

    @Test
    public void testGetOrder() throws Exception {
        ErrorResponseFilter errorResponseFilter = new ErrorResponseFilter();
        assertEquals(0, errorResponseFilter.getOrder(), "getOrder should return 0");
    }
}