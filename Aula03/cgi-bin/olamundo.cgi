#!/bin/bash
echo "Content-type: text/html"
echo
echo "
<html>
	<head><title>CAI - Tarde</title></head>

	<body>
		<h1><center>Olá mundo - SSH</center></h1>
"
for x in {1..20}; do
	echo "<h5> Olá mundo número: $x </h5>"
done

echo "
	</body>
</html>
"
