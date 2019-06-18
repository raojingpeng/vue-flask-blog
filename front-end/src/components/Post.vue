<template>
  <v-container>
    <v-layout>
      <!-- <v-flex
        md12
        xs2
        style="position: absolute; top: 21px; right: 0px;"
      >
        <v-btn color="primary">Editor
          <v-icon right>edit</v-icon>
        </v-btn>
        <v-btn color="warning">Delete
          <v-icon right>delete</v-icon>
        </v-btn>

      </v-flex> -->


      <v-flex xs12>
        <!-- <mavon-editor v-model="value" style="position: initial; max-height:600px;" /> -->
        <div
          v-html="post.body"
          class="markdown-body"
        ></div>
        <!-- <div v-if="sharedState.user_id === post.author.id" style="float: right">
          <p>1</p>
        </div> -->
      </v-flex>



    </v-layout>
  </v-container>
</template>

<script>
import store from '../store.js'

export default {
  name: 'Post',
  data() {
    return {
      sharedState: store.state,
      post: {
        author: {
          id: ''
        }
      }
    }
  },
  methods: {
    getPost(id) {
      const path = `/posts/${id}`
      this.$axios
        .get(path)
        .then(response => {
          this.post = response.data
        })
        .catch(error => {
          console.log(error)
        })
    }
  },
  created() {
    const id = this.$route.params.id
    this.getPost(id)
  },
  // 当查询参数 page 或 per_page 变化后重新加载数据
  beforeRouteUpdate(to, from, next) {
    console.log('Post RouterUpdate')
    this.getPost(to.params.id)
  }
}
</script>








