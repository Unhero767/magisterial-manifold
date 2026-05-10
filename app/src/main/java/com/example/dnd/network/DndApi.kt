package com.example.dnd.network

import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory

object DndApi {
    private const val BASE_URL = "https://www.dnd5eapi.co/"

    private val retrofit = Retrofit.Builder()
        .baseUrl(BASE_URL)
        .addConverterFactory(GsonConverterFactory.create())
        .build()

    val service: DndApiService = retrofit.create(DndApiService::class.java)
}