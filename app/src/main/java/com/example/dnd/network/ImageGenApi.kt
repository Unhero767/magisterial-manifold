package com.example.dnd.network

import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory

object ImageGenApi {
    private const val BASE_URL = "https://api.deepai.org/"

    private val retrofit = Retrofit.Builder()
        .baseUrl(BASE_URL)
        .addConverterFactory(GsonConverterFactory.create())
        .build()

    val service: ImageGenApiService = retrofit.create(ImageGenApiService::class.java)
}