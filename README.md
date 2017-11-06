# rektus
An algorithm simulating changes in population and such.

# version 1.0 / initial commit
working, not stable

# TODO:
~~fix error for population <2~~ implement a more efficient reproduction system that prevents dieing out <br>
~~code correction, re-evaluate syntax, esp. while, (gauss-normalization in some random parameters?)~~<br>

<br>
rektus.py: <br>
average(): height for both sexes, max gen, (min/max height?)<br>
date(): re-evaluate for better efficiency , esp. for larger population groups --> store data in files to clear up ram? <br>
and/or make more realistic using different parameters like wealth, health, power, age, intelligence<br>
<br>
person.py: <br>
make health inheritable, see general changes<br>
<br>
# done:
rektus.py: <br>
average(): ftm ratio as real ratio, current population counter<br>
<br>
# Ideas for future releases:
rework overall lifecycle including inheritable health and more realistic reproduction/dating behavior<br>
conclusion of a generation, average() per generation instead of iteration, -->average(gen)?<br>
->new class generation?<br>
add more inheritable parameters like eye/hair colour <br>
add random events (diseases, catastrophes, wars, religion(how?), donald trump, etc) <br>
add a bunch of commands to manipulate parameters while in simulation (settings file?) <br>
add a more graphic way to display values, 
-> build standalone program with ui, graphing<br>
