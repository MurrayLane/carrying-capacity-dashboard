<%-- 
    Document   : forum
    Created on : 28/11/2011, 10:56:16 AM
    Author     : sebasti2
--%>
<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
  <meta property="fb:app_id" content="354192454610075"/>
  <title>Carrying Capacity Dashboard User Forum</title>
  <link href='//fonts.googleapis.com/css?family=Oswald:700' rel='stylesheet' type='text/css'>
  <link type="text/css" href="css/overcast/jquery-ui-1.8.16.custom.css" rel="stylesheet" />	
  <link rel="stylesheet" href="css/common.css" type="text/css" />
  <link rel="stylesheet" href="css/dashboard.css" type="text/css" />
  
  <script type="text/javascript" src="//ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js"></script>
  <script type="text/javascript" src="//ajax.googleapis.com/ajax/libs/jqueryui/1.8.16/jquery-ui.min.js"></script>
  <script type="text/javascript" src="js/dashboard.js"></script>

  <!-- Google Analytics Script -->
  <script type="text/javascript">
  var _gaq = _gaq || [];
  _gaq.push(['_setAccount', 'UA-30398336-1']);
  _gaq.push(['_setDomainName', '.carryingcapacity.com.au']);
  _gaq.push(['_trackPageview']);

  (function() {
    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
  })();
  </script>
</head>

<body>
<div class="header-container">
  <div class="header-content content-center">
    <div class="left">
      <div class="title"><div class="c1">CARRYING&nbsp;</div><div class="c2">CAPACITY&nbsp;</div><div class="c3">DASHBOARD</div><div class="c4">&nbsp;USER FORUM</div></div>
      <div class="subtitle">A resource-based indicator of regional self sufficiency</div>
    </div>
    <div class="notice">
      <h3>PROTOTYPE DASHBOARD ONLY</h3>
      <p>While every effort has been made to ensure its accuracy, <br/> the developers accept no liability for any results generated.</p>
      <h3>CARRYING CAPACITY DASHBOARD</h3>
      <p>Go back to the <a href=".">Dashboard</a>.</p>
    </div>
  </div>
</div>
  
<div class="main-container">
  <div class="content-center">
    <div class="main-content">
      
      <div id="fb-root"></div>
      <script>
        (function(d, s, id) {
          var js, fjs = d.getElementsByTagName(s)[0];
          if (d.getElementById(id)) return;
          js = d.createElement(s); js.id = id;
          js.src = "//connect.facebook.net/en_US/all.js#xfbml=1&appId=354192454610075";
          fjs.parentNode.insertBefore(js, fjs);
          }(document, 'script', 'facebook-jssdk'));
      </script>

      <div id="forum">
        <p>Don’t have a Facebook, Yahoo, Hotmail or AOL account? Just email your comment or question to <a href="mailto:mc.lane@qut.edu.au">mc.lane@qut.edu.au</a>.</p>
        <p>When sending the email please advise if you wish the correspondence to remain private or it may be posted in the comments section by the moderator.</p>
        <a name="forum"></a>
        <div class="fb-comments" data-href="http://dashboard.carryingcapacity.com.au" data-num-posts="50" data-width="1100"></div>
      </div>
      
    </div><!--main-content-->
  </div><!--content-center-->
</div><!--main-container-->
  
<div class="footer-container">
  <div class="footer-content content-center"></div>
</div>

</body>

</html>