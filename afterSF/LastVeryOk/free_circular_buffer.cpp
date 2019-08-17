#include "free_circular_buffer.h"
#include <iostream>


Free_Circular_Buffer::Free_Circular_Buffer(size_t size) : size(size){
	this->free_circular_buffer = (void**) malloc(this->size*sizeof(void*));
	for(size_t i = 0; i < this->size; i++)
		this->free_circular_buffer[i] = NULL;
	this->d_mutex = new std::mutex();
	return;
}

Free_Circular_Buffer::~Free_Circular_Buffer(){
	delete [] this->free_circular_buffer;
	delete this->d_mutex;
	return;
}

bool Free_Circular_Buffer::safe_push(void* const task){
	if(this->free_circular_buffer[this->p_write] == NULL){
		std::atomic_thread_fence(std::memory_order_release);
		this->free_circular_buffer[p_write] = task;
		//std::cout << p_write << std::endl;
		this->p_write = (this->p_write == this->size - 1) ? 0 : this->p_write + 1;
		return true;
	}
	return false;
}

/*
bool Free_Circular_Buffer::try_safe_push(void* const task){
	std::unique_lock<std::mutex> lock(*d_mutex, std::try_to_lock);
	if(lock.owns_lock()){
		this->circular_buffer[p_write] = task;
		this->p_write = (this->p_write == this->size - 1) ? 0 : this->p_write + 1;
		this->c_condition->notify_one();
		return true;
	}
	return false;
}
*/

bool Free_Circular_Buffer::safe_pop(void** task){
	if(this->free_circular_buffer[this->p_read] != NULL){  
		*task = this->free_circular_buffer[this->p_read];
		std::atomic_thread_fence(std::memory_order_acquire);
		this->free_circular_buffer[this->p_read] = NULL;
		this->p_read = (this->p_read == this->size - 1) ? 0 : this->p_read + 1;
		return true;
	}
	return false;
}


void Free_Circular_Buffer::safe_resize(size_t new_size){
	std::lock_guard<std::mutex> lock(*d_mutex);
	this->size = new_size;
	this->free_circular_buffer = (void**) realloc (this->free_circular_buffer, new_size*sizeof(void*));
	return;
}


size_t Free_Circular_Buffer::safe_get_size(){
	std::lock_guard<std::mutex> lock(*d_mutex);
	return this->size;
}

