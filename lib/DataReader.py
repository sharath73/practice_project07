from lib.configreader import appconfig




def courses_schema():
    c_schema = "course_id long,course_name string,category string,duration_hours string"
    return c_schema

def read_courses(spark,env):
    cf =appconfig(env)
    courses_file_path =cf["courses"] 
    return spark.read \
    .format("csv") \
    .option("header","true") \
    .schema(courses_schema()) \
    .load(courses_file_path)

def students_Schema():
    s_schema ="student_id long,first_name string,last_name string,city string"
    return s_schema

def read_students(spark,env):
     sf= appconfig(env)
     students_file_path = sf["students"] 
     return spark.read \
    .format("csv") \
    .option("header","true") \
    .schema(students_Schema()) \
    .load(students_file_path)

def enrollments_schema():
    e_schema ="enrollment_id long,student_id long,course_id long,enrollment_date string,status string"
    return e_schema

def read_enrollments(spark,env):
     ef= appconfig(env)
     students_file_path = ef["enrollments"] 
     return spark.read \
    .format("csv") \
    .option("header","true") \
    .schema(enrollments_schema()) \
    .load(students_file_path)