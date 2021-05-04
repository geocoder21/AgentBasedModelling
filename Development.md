## Testing
Testing was completed as the code was developed, with most issues corrected as they emerged.  For example, in order for the 'eat_sheep' function to work correctly the number of sheep had to be reduced.  This was achieved through a new sheep_left variable.

Testing was also carried out using the print function at critical points within the programme.  These were then commented out and annoted as test code.

A doctest module was included and run through Command Prompt as the code was developed.

## Known issues 
#### Parameters
Parameters can be manually adjusted within the code.  If these are significantly increased then processing requirements are increased and the code is slow to run.  Where parameters are set to zero this prevents correct execution. The final 'model_sliders' version addresses this by creating maximum and minimum numbers of sheep and wolves, however the code can still be manipulated.

#### No sheep left
If all the sheep have been eaten the wolves continue to move around the environment for the required number of iterations, however the sheep loop within 'update' in unable to complete. This can lead to a hung programme.

#### Figure 1
When the model is executed through Spyder the animation runs within the GUI, but a second pane (labelled Figure 1) also opens as a blank window.  The programme runs correctly through Command Prompt, and since efforts to remove this issue broke the code it is currently an accepted issue.

## Ideas for further development

1.  A number of global variables are currently used in order to share values between functions, however there is potential to refactor the code to remove some of these.

2.  Introduction of an error message if parameters set to 0, or excessively high.

3.  Code could be introduced into the programme to stop execution when a set number of sheep were left, or no sheep are left

4.  Sheep stores could be plotted on a graph using matplotlib since these are captured when the model is run.

5.  Removal of the superfluous 'Figure 1' pane when the programme is run in Spyder.
