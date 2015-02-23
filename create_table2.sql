DROP TABLE IF EXISTS coursedata;
CREATE TABLE coursedata (
   deptNum int,
   courseNum int,
   semester int,
   meetingType text,
   seatsTaken int,
   seatsOffered int,
   instructorNum int
 );
 
 CREATE TABLE profdata (
   instructorNum INTEGER AUTOINCREMENT,
   instructor text

 );
 
  CREATE TABLE deptdata (
   instructorNum INTEGER AUTOINCREMENT,
   dept text
 );