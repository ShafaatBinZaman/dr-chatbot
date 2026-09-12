import 'package:flutter/material.dart';
import 'package:firebase_core/firebase_core.dart';
import 'login_signup_choice.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp();  // Initialize Firebase
  runApp(DrChatbotApp());
}

class DrChatbotApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Dr. Chatbot',
      theme: ThemeData(
        primaryColor: Colors.green,  // Use greenish color theme
      ),
      home: LoginSignUpChoicePage(),  // Show the first screen with sign-up/login options
    );
  }
}
