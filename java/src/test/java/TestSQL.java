import org.apache.spark.sql.SparkSession;
import org.junit.Test;

public class TestSQL {

    @Test
    public void testMyCounter() {
        SparkSession spark = SparkSession
            .builder()
            .appName("Build a DataFrame from Scratch")
            .master("local[*]")
            .getOrCreate();

        spark.sql("select 1").createOrReplaceTempView("v");
        spark.sql("select * from v").createOrReplaceTempView("v");
    }

}