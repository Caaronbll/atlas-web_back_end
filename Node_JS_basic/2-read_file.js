// 2-read_file.js

const fs = require('fs');

function countStudents(path) {
  if (!fs.existsSync(path)) {
    throw new Error('Cannot load the database');
  }

  const data = fs.readFileSync(path, 'utf8');
  const students = data.trim().split('\n').slice(1); // Directly omit header
  const studentsByField = {};

  students.forEach((student) => {
    const [firstName,, , field] = student.split(',');
    if (!studentsByField[field]) studentsByField[field] = [];
    studentsByField[field].push(firstName);
  });

  const totalStudents = students.length;
  console.log(`Number of students: ${totalStudents}`);

  Object.entries(studentsByField).forEach(([field, names]) => {
    console.log(`Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`);
  });
}

module.exports = countStudents;
