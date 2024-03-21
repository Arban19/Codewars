"""
It's the academic year's end, fateful moment of your school report.
The averages must be calculated.
All the students come to you and entreat you to calculate their average for them.
Easy ! You just need to write a script.

Return the average of the given array rounded down to its nearest integer.

The array will never be empty.

"""
fn get_average(marks: &[i32]) -> i32 {
    let sum: i32 = marks.iter().sum();
    let len = marks.len() as i32;
    let average = sum / len;
    average
}
