package com.example.dnd.network

import retrofit2.http.GET

interface DndApiService {
    @GET("api/monsters")
    suspend fun getMonsters(): MonsterListResponse
}

data class MonsterListResponse(
    val results: List<MonsterReference>
)

data class MonsterReference(
    val index: String,
    val name: String,
    val url: String
)