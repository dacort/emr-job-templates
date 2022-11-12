
/* SimpleApp.java */
import org.apache.spark.sql.SparkSession;

public class SimpleApp {
    public static void main(String[] args) {
        SparkSession spark = SparkSession.builder().appName("Simple Application").getOrCreate();

        spark.sql("select 1").createOrReplaceTempView("v");
        spark.sql("select * from v").createOrReplaceTempView("v");

        System.out.println("Just a demo");
    }
}