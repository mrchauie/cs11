<?php

$username  = $_COOKIE['username'];
$query = $db -> query ("SELECT * FROM $db_users WHERE id = $username");
$userrecord = $query -> fetch_record();
>



<?php
$cart = new CartItem
...
if $_REQUEST['action'] == 'removeCartItem' && !empty($_REQUEST['id'])) {
    remove($cart, $_REQUEST['id']);
    header('view_cart.php');
}
>

<!DOCTYPE html>
<html>
<body>
<h3>Search for a skate</h3>
<form action='search.php' method="post">
    <select name="brand">
    <option>Bauer</option>
    <option>CCM</option>
    <option>K2</option>
    <option>Reebok</option>
    </select>
    <select name="size">
    <option>6</option>
    <option>7</option>
    <option>8</option>
    <option>9</option>
    <option>10</option>
    <option>11</option>
    </select>
    <input type='submit' value='Search' />
</form>
</body>
</html>






</>