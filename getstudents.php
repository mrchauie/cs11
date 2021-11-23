<html>


<?php
$db = new SQLite3('students.db');
$res = $db->query('SELECT * FROM students');
while ($row = $res->fetchArray()) {
    echo "{$row[0]} {$row[1]} {$row[2]}";?><br>
<?php }?>

</html>