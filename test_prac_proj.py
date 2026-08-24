import pytest
from lib.DataManipulation import *
from lib.DataReader import *
from lib.Utility import *

@pytest.mark.transformation
def test_count_dataengineering(spark):
    course_df = read_courses(spark,"Loc")
    count_d = count_dataengineering(course_df)
    assert count_d == 6

@pytest.mark.parametrize("enrl_status,count",
                         [("Active",8),("Completed",4)]
                         )
def test_count_enrollments(spark,enrl_status,count):
    enrollments_df  =read_enrollments(spark,"Loc") 
    enrl_counts = count_enrollments(enrollments_df,enrl_status)
    assert  enrl_counts == count