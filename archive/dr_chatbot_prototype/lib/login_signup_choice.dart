import 'package:flutter/material.dart';
import 'login_screen.dart';
import 'signup_screen.dart';

class LoginSignUpChoicePage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Row(
          children: [
            Image.asset(
              'assets/dr_chatbot_logo.png',  // Add the logo image
              height: 30,
            ),
            SizedBox(width: 10),
            Text('Dr. Chatbot'),
          ],
        ),
        backgroundColor: Colors.green, // Green app bar
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            ElevatedButton(
              onPressed: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(builder: (context) => SignUpPage()),
                );
              },
              style: ElevatedButton.styleFrom(
                backgroundColor: Colors.green,  // Set button color
                minimumSize: Size(double.infinity, 50),  // Full width button
              ),
              child: Text('Sign Up'),
            ),
            SizedBox(height: 20),
            ElevatedButton(
              onPressed: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(builder: (context) => LoginPage()),
                );
              },
              style: ElevatedButton.styleFrom(
                backgroundColor: Colors.blue,  // Set button color
                minimumSize: Size(double.infinity, 50),  // Full width button
              ),
              child: Text('Login'),
            ),
          ],
        ),
      ),
    );
  }
}
