package com.example.dnd.network

import okhttp3.RequestBody
import retrofit2.http.Body
import retrofit2.http.Header
import retrofit2.http.POST

data class ImageGenRequest(
    val text: String
)

data class ImageGenResponse(
    val output_url: String
)

interface ImageGenApiService {
    @POST("api/stable-diffusion")
    suspend fun generateImage(
        @Header("api-key") apiKey: String,
        @Body request: ImageGenRequest
    ): ImageGenResponse
}