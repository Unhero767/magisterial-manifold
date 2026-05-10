package com.example.dnd

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.Image
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.Button
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.rememberCoroutineScope
import androidx.compose.runtime.setValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import coil.compose.rememberImagePainter
import com.example.dnd.ui.generateImage
import com.example.dnd.ui.generatePrompt
import com.example.dnd.ui.theme.DNDTheme
import kotlinx.coroutines.launch

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            DNDTheme {
                Surface(modifier = Modifier.fillMaxSize(), color = MaterialTheme.colorScheme.background) {
                    DndApp()
                }
            }
        }
    }
}

@Composable
fun DndApp() {
    var prompt by remember { mutableStateOf("Tap the button to generate a prompt!") }
    var imageUrl by remember { mutableStateOf<String?>(null) }
    val coroutineScope = rememberCoroutineScope()

    Column(modifier = Modifier.padding(16.dp)) {
        Text(text = prompt)
        Spacer(modifier = Modifier.height(16.dp))
        Button(onClick = { 
            coroutineScope.launch {
                prompt = generatePrompt()
                imageUrl = generateImage(prompt)
            }
        }) {
            Text("Generate Prompt and Image")
        }
        Spacer(modifier = Modifier.height(16.dp))
        imageUrl?.let {
            Image(
                painter = rememberImagePainter(data = it),
                contentDescription = null
            )
        }
    }
}

@Preview(showBackground = true)
@Composable
fun DefaultPreview() {
    DNDTheme {
        DndApp()
    }
}
