import org.junit.Test;

import static org.junit.Assert.*;

public class SumOfProperElementsTest {

    @Test
    public void sumOfProperElements() {
        assertEquals(9,SumOfProperElements.sumOfProperElements(new int[]{1,2,6}));
        assertEquals(10,SumOfProperElements.sumOfProperElements(new int[]{10,25}));
    }
}
