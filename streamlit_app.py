import pandas
import streamlit

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list.set_index("fruit")

streamlit.multiselect("Pick some fruits: ", list(my_fruit_list.index))

# data source display
streamlit.dataframe(my_fruit_list)
