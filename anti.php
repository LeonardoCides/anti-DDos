<?php 
// anti ddos script using php 


$IPmaxNumber = 10;


$clientIP = $_SERVER['HTTP_CLIENT_IP'] ? $_SERVER['HTTP_CLIENT_IP'] : 
            ($_SERVER['REMOTE_ADDR'] ? $_SERVER['REMOTE_ADDR'] : 
            ($_SERVER['HTTP_X_FORWARDED_FOR'] ? $_SERVER['HTTP_X_FORWARDED_FOR'] : 
            $_SERVER['REMOTE_ADDR']));


$IPs = file_get_contents('loggedIP.txt');


if (strstr($IPs, $clientIP)) {
    
    $ips = explode(',', $IPs);

    
    if (count($ips) > $IPmaxNumber) {
        header("HTTP/1.0 403 Forbidden");
        exit;
    }
    
    array_push($ips, $clientIP);
    
    file_put_contents('loggedIP.txt', implode(",", $ips));
}
