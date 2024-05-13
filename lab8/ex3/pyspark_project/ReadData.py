class ReadData:
    def __init__(self, spark):
        self.spark = spark

    def read_csv(self, filepath):
        return self.spark.read.format("csv").option("header", "true").option("inferSchema", "true").load(filepath)