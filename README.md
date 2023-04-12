To use it you have to download last ai class's pdf and rename it 'score.pdf'
then type 'python3 main.py reload' to update the .json file.

Once json is updated, you can use several options:

Always start with 'python3', then you can add :
 
- 'reload' to refresh json file
- 'score' to get the ranking of all students
- 'score --student_id--' to get --student_id-- score and ranking

- 'display' and then add the following :
    - 'bar' or 'line' to specify the type of graph
    - a float to specify precision of graph
    - (optionnal) add student_id to see it on the graph

example : 'python3 display line 1.25 230ADB029' // 'python3 scores' // 'python3 display bar 0.7'

De rien Paul


PS : Import the library with pip or it won't work (obviously cyka)
