## Testing
Testing was completed as the code was developed, with most issues corrected as they emerged.  For example, in order for the 'eat_sheep' function to work correctly the number of sheep had to be reduced.  This was achieved through a new sheep_left variable.

Testing was also carried out using the print function at critical points within the programme.  These were then commented out and annoted as test code.

## Known issues 
#### Parameters
Parameters can be manually adjusted within the code.  If these are significantly increased then processing requirements are increased and the code is slow to run.  Where parameters are set to zero this prevents correct execution. 
#### Figure 1
When the model is executed through Spyder the animation runs within the GUI, but a second pane (labelled Figure 1) also opens as a blank window.  The programme runs correctly through Command Prompt, and since efforts to remove this issue broke the code it is currently an accepted issue.

## Ideas for further development

1.  Parameters could be adjusted by the user by including sliders within the GUI - for example to select number of sheep and wolves.  This would also correct the parameter issues identified above.

2.  Code could be introduced into the programme to stop execution when a set number of sheep were left.

3.  Sheep stores could be plotted on a graph using matplotlib since these are captured when the model is run.

4.  Removal of the superfluous 'Figure 1' pane.
