<template>
	<div class="catalog container is-fullhd">
		
		<b-table :data="info" :selected.sync="selected" :striped="true" :fullWidth="true">

			<template scope="props" slot="header">
			   <div style="width: 100%" class="has-text-centered">
			     {{ props.column.label }}
			   </div>
			</template>	

			<template slot-scope="props">
				<b-table-column label="Clave corta" >
				  {{ props.row.fields.cve_corta }}
				</b-table-column>
				<b-table-column label="Razon Social"  >
				  {{ props.row.fields.razon_social }}
				</b-table-column>
				<b-table-column label="Consecutivo" centered  numeric >
				  {{ props.row.fields.consecutivo }}
				</b-table-column>
				<b-table-column label="Observaciones"  >
				  {{ props.row.fields.observaciones }}
				</b-table-column>
			</template>

			<template slot="empty">
			  <section class="section">
			      <div class="content has-text-grey has-text-centered">
			          <p>
			              <b-icon
			                  icon="sentiment_very_dissatisfied"
			                  size="is-large">
			              </b-icon>
			          </p>
			          <p>No existe informacion</p>
			      </div>
			  </section>
			</template>
		</b-table>	
	</div>
</template>

<script>
	import searchContainer from "./searchContainer.vue"
	import axios from 'axios';

	export default{
		props: ['info'],
		data() {
			return {
				currentDate: new Date(),
				selected: {},
				list: [
				  {
				    title: "Una carta",
				    time: self.currentDate,
				    btn: "Detalle"
				  },
				  {
				    title: "Una carta de algo",
				    time: self.currentDate,
				    btn: "Detalle"
				  },
				  {
				    title: "Entendimiento",
				    time: self.currentDate,
				    btn: "Detalle"
				  },
				  {
				    title: "Algo de refexion",
				    time: self.currentDate,
				    btn: "Detalle"
				  },
				  {
				    title: "Una carta",
				    time: self.currentDate,
				    btn: "Detalle"
				  },
				  {
				    title: "Una carta",
				    time: self.currentDate,
				    btn: "Detalle"
				  },
				  {
				    title: "Una carta",
				    time: self.currentDate,
				    btn: "Detalle"
				  },

				],
			}
		},
		created() {
		   axios.get(`http://localhost:8000/oficinas/`)
		   .then(response => {
		     // JSON responses are automatically parsed.
		     this.list = JSON.parse(response.data)
		   })
		   .catch(e => {
		     this.errors.push(e)
		   })
		}
	}
</script>

<style>
	table{
		width: 100%;
	}
</style>