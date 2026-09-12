import 'package:firebase_core/firebase_core.dart';
import 'package:flutter/material.dart';
import 'firebase_options.dart';  


import 'screens/home_screen.dart';
import 'screens/login_screen.dart';
import 'screens/signup_screen.dart';  


void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp(
    options: DefaultFirebaseOptions.currentPlatform,  
  );
  runApp(DrChatbotApp());
}


class DrChatbotApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Dr Chatbot',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(primarySwatch: Colors.teal),


     
      routes: {
        '/home': (context) => HomeScreen(),
        '/login': (context) => LoginScreen(),
        '/signup': (context) => SignupScreen(),
        '/chat': (context) => ChatPage(),
      },


      initialRoute: '/home',
    );
  }
}




class ChatPage extends StatefulWidget {
  @override
  _ChatPageState createState() => _ChatPageState();
}


class _ChatPageState extends State<ChatPage> {
  final TextEditingController _controller = TextEditingController();
  final List<Map<String, String>> _messages = [];


  Future<void> sendMessage(String text) async {
    setState(() => _messages.add({'sender': 'user', 'text': text}));


    try {
      final response = await http.post(
        Uri.parse('https://vile-nikia-unsplendorously.ngrok-free.dev/chat'),
        headers: {'Content-Type': 'application/json'},
        body: json.encode({'message': text}),
      );


      if (response.statusCode == 200) {
        final data = json.decode(response.body);
        setState(() => _messages.add({
              'sender': 'bot',
              'text': data['bot'] ?? data['advice'] ?? '🤖 No response',
            }));
      } else {
        setState(() => _messages.add({
              'sender': 'bot',
              'text': '❌ Server error: ${response.statusCode}',
            }));
      }
    } catch (e) {
      setState(() => _messages.add({
            'sender': 'bot',
            'text': '⚠️ Connection failed: $e',
          }));
    }
  }


  @override
  Widget build(BuildContext context) => Scaffold(
        appBar: AppBar(title: Text('Dr Chatbot')),
        body: Column(
          children: [
            Expanded(
              child: ListView.builder(
                itemCount: _messages.length,
                itemBuilder: (ctx, i) {
                  final m = _messages[i];
                  return Align(
                    alignment: m['sender'] == 'user'
                        ? Alignment.centerRight
                        : Alignment.centerLeft,
                    child: Container(
                      margin: EdgeInsets.all(8),
                      padding: EdgeInsets.all(12),
                      decoration: BoxDecoration(
                        color: m['sender'] == 'user'
                            ? Colors.teal[100]
                            : Colors.grey[300],
                        borderRadius: BorderRadius.circular(12),
                      ),
                      child: Text(m['text'] ?? ''),
                    ),
                  );
                },
              ),
            ),
            Padding(
              padding: EdgeInsets.all(8),
              child: Row(
                children: [
                  Expanded(
                    child: TextField(
                      controller: _controller,
                      decoration: InputDecoration(hintText: 'Type your symptom...'),
                    ),
                  ),
                  IconButton(
                    icon: Icon(Icons.send),
                    onPressed: () {
                      final text = _controller.text.trim();
                      if (text.isNotEmpty) {
                        sendMessage(text);
                        _controller.clear();
                      }
                    },
                  ),
                ],
              ),
            )
          ],
        ),
      );
}
