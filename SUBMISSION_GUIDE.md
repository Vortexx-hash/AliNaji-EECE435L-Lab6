# Lab 6 submission instructions

Only Exercise 1 is graded. Exercise 2 and its Makefile are omitted as requested.
The handout asks for the complete PyBuilder project and a terminal screenshot.
It does not request a separate written report for Exercise 1.

## What was implemented

- Project and module name: `calculator_Ali_Naji` (using Ali Naji as the name).
- Original operations: add, subtract, multiply, divide.
- Graded extensions: modulus, power, square_root.
- Error handling for division/modulus by zero and square root of a negative number.
- 25 unit tests, including normal, decimal, negative, and invalid inputs.
- `build.py` with working test discovery, project metadata, and local packaging.
- `requirements.txt` pinning the installed PyBuilder version.
- `README.md` with setup commands and an explanation of the build process.
- Saved terminal build output in the project's `evidence` directory.
- Verified both `pyb run_unit_tests` and the default `pyb` build: both reported
  `BUILD SUCCESSFUL`, with 25 tests passing and zero failures or errors.
- Built a wheel and source archive, then imported the wheel and checked all
  seven operations. Both artifacts are in the submissioln ZIP.

The supplied assignment Word document was not changed.

## Take the required screenshot

1. Open PowerShell or the VS Code terminal. Maximize it and use a readable font.
2. Run these commands using the environment already installed in this workspace:

```powershell
cd 'C:\Users\AliNaji\Desktop\EECE435L\Lab6\calculator_Ali_Naji'
..\.venv\Scripts\pyb.exe run_unit_tests
```

3. Capture the actual terminal after it finishes. Include ALL these details:

   - The `run_unit_tests` command (if necessary, reduce the font slightly).
   - A result showing that 25 tests ran successfully with no errors/failures.
   - `BUILD SUCCESSFUL`.
   - The `Build finished at ...` line.
   - The `Build took ...` line, showing elapsed time.
   - `Base directory: ...\calculator_ali_naji` (PyBuilder normalizes the Windows
     path to lowercase; the Project line still shows `calculator_Ali_Naji`).

4. Use Windows Snipping Tool (`Win+Shift+S`) and save the screenshot as
   `Lab6_Ali_Naji_PyBuilder.png` in this Lab6 folder. Check the saved image is
   readable and that the base directory and timing lines are not cut off.

One screenshot is enough if all the above fits. If it does not fit legibly,
take a second screenshot for the test summary. The required footer screenshot
must show the build finish, time taken, and named base directory together.
The saved text logs supplement the screenshot; they do not replace it.

Optional additional evidence: run `..\.venv\Scripts\pyb.exe` and screenshot its
successful packaging result. The handout explicitly requires the successful
PyBuilder terminal screenshot, not screenshots of every source file or test.

## Upload to Moodle

Upload these two files:

1. `calculator_Ali_Naji_submission.zip`: the complete source project with
   `build.py`, `requirements.txt`, `README.md`, `src`, `tests`, and saved evidence.
   The built wheel and source archive are included in `artifacts`.
2. `Lab6_Ali_Naji_PyBuilder.png`: your actual terminal screenshot from above
   (and the second test-summary screenshot only if needed for readability).

If Moodle only allows one file, put the project ZIP and screenshot into one
outer ZIP and upload that. Do not submit `.venv`, `.pybuilder`, `__pycache__`,
or the assignment handout. Those are not needed to reproduce the project.

If Ali Naji is not your submission name, update the project folder, source and
test package names, imports, metadata and configured test path in `build.py`,
then rerun the tests and regenerate the ZIP and screenshot before submission.
