<template>
	<div class="container ">
		<slot name="form"></slot>
	</div>
</template>

<script>
	export default{
		methods: {
			search: function(){
				console.log("Buscando...")
			}
		}
	}
</script>

<style>
	
</style>