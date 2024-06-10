<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple Shop</title>
</head>

<body>
    <h1>Simple Shop</h1>
    <form id="orderForm">
        <label for="name">Name:</label><br>
        <input type="text" id="name" name="name" required><br>
        <label for="email">Email:</label><br>
        <input type="email" id="email" name="email" required><br>
        <label for="product">Product:</label><br>
        <input type="text" id="product" name="product" required><br>
        <button type="submit">Purchase</button>
    </form>

    <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
    <script>
        const form = document.getElementById('orderForm');

        form.addEventListener('submit', function (event) {
            event.preventDefault();
            const formData = new FormData(this);

            axios.post('process_order.php', formData)
                .then(function (response) {
                    console.log(response.data);
                    alert('Order placed successfully!');
                    // You can redirect the user to a thank you page or do any other action here
                })
                .catch(function (error) {
                    console.error(error);
                    alert('An error occurred. Please try again later.');
                });
        });
    </script>

    <?php
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $name = $_POST['name'];
        $email = $_POST['email'];
        $product = $_POST['product'];

        $to = 'thaisang3259@gmail.com';
        $subject = 'New Order';
        $message = "Name: $name\n";
        $message .= "Email: $email\n";
        $message .= "Product: $product\n";

        $headers = 'From: webshop@example.com' . "\r\n" .
            'Reply-To: webshop@example.com' . "\r\n" .
            'X-Mailer: PHP/' . phpversion();

        mail($to, $subject, $message, $headers);
        echo 'Email sent successfully!';
    }
    ?>
</body>

</html>