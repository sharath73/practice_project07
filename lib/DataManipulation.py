from pyspark.sql.functions import *
from pyspark.sql.functions import col

def count_dataengineering(courses_df):
    return courses_df.filter("course_name = 'Data Engineering'").count()

def count_enrollments(enrollments_df,enrl_status):
    return enrollments_df.filter(col("status") == enrl_status).count()


def student_enrollment_id(students_df,enrollments_df):
    return students_df.join(enrollments_df,"student_id","inner")
