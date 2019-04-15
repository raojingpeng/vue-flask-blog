<template>
    <div class="container">
        <alert
          v-for="(alert, index) in activeAlert" :key="index"
          :variant="alert.alertVariant"
          :message="alert.alertMessage">
        </alert>
    </div>
</template>

<script>
import Alert from './Alert'

export default {
    name: 'Home',
    components: {
        alert: Alert
    },
    data: () => {
        return {
            alerts: [
                {
                    showAlert: true,
                    alertVariant: 'danger',
                    alertMessage: 0
                },
                {
                    showAlert: true,
                    alertVariant: 'info',
                    alertMessage: 1
                },
                {
                    showAlert: true,
                    alertVariant: 'dark',
                    alertMessage: 2
                },
                {
                    showAlert: false,
                    alertVariant: 'danger',
                    alertMessage: 'test'
                }
            ]
        }
    },
    computed: {
        activeAlert: function () {
            return this.alerts.filter(function (alert) {
                return alert.showAlert
            })
        }
    }
}
</script>

