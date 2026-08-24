import sys
from lib import configreader,DataReader,DataManipulation,Utility
from pyspark.sql.functions import *

if __name__=="__main__":
    if len(sys.argv)<2:
        print("please specify the environment")
        sys.exit(-1)

    job_run_env = sys.argv[1]

    print("Creating spark_session")

    spark = Utility.sprk_session(job_run_env)

    print("spark session is created")

    courses_df = DataReader.read_courses(spark,job_run_env)
    enrollments_df  = DataReader.read_enrollments(spark,job_run_env)
    students_df  = DataReader.read_students(spark,job_run_env)

    cnt_de = DataManipulation.count_dataengineering(courses_df)

    print(cnt_de)

    cnt_enr = DataManipulation.count_enrollments(enrollments_df,enrl_status='Active')

    print(cnt_enr)

    student_enrl_id = DataManipulation.student_enrollment_id(students_df,enrollments_df)
    student_enrl_id.show()

    print("end of main")