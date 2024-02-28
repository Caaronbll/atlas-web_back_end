// 2-read_file.js

const fs = require('fs');

function countStudents(path) {
  try {
    // Read the database file synchronously
    const data = fs.readFileSync(path, 'utf8');

    // Split the data into rows
    const rows = data.trim().split('\n');

    // Check if there are any rows in the file
    if (rows.length === 0) {
      throw new Error('No students found in the database.');
    }

    // Initialize counters for each field
    let mathCount = 0;
    let CSCount = 0;

    // Initialize arrays to store first names for each field
    const mathFirstNames = [];
    const CSFirstNames = [];

    // Loop through each row
    for (const row of rows) {
      // Split the row into fields
      const [firstName, age, field] = row.split(',');

      // Check if the row is valid
      if (firstName && age && field) {
        // Increment the respective field counter
        if (field === 'CS') {
          CSCount++;
          CSFirstNames.push(firstName);
        } else if (field === 'Math') {
          mathCount++;
          mathFirstNames.push(firstName);
        }
      }
    }

    // Log the number of students in each field and the list of first names
    console.log(`Number of students in CS: ${CSCount}. List: ${CSFirstNames.join(', ')}`);
    console.log(`Number of students in Math: ${mathCount}. List: ${mathFirstNames.join(', ')}`);
    console.log(`Number of students: ${CSCount + mathCount}`);
  } catch (error) {
    // Handle errors, log the error message
    console.error(`Error: ${error.message}`);
  }
}

module.export = countStudents;
