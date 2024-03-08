"""
Write function bmi that calculates body mass index (bmi = weight / height2).

if bmi <= 18.5 return "Underweight"

if bmi <= 25.0 return "Normal"

if bmi <= 30.0 return "Overweight"

if bmi > 30 return "Obese"

"""

fn bmi(weight: u32, height: f32) -> &'static str {
    let bmi = weight as f32 / (height * height);
    match bmi {
      bmi if bmi <= 18.5 => "Underweight",
      bmi if bmi <= 25.0 => "Normal",
      bmi if bmi <= 30.0 => "Overweight",
      _ => "Obese"
    }
  }
