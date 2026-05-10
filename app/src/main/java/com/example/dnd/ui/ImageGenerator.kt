package com.example.dnd.ui

import com.example.dnd.BuildConfig
import com.example.dnd.network.ImageGenApi
import com.example.dnd.network.ImageGenRequest

suspend fun generateImage(prompt: String): String? {
    return try {
        val response = ImageGenApi.service.generateImage(
            apiKey = BuildConfig.IMAGE_API_KEY,
            request = ImageGenRequest(text = prompt)
        )
        response.output_url
    } catch (e: Exception) {
        e.printStackTrace()
        null
    }
}