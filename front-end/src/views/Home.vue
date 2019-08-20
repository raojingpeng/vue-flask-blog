<template>
  <v-container grid-list-lg>
    <v-layout
      row
      wrap
    >
      <v-flex
        xs12
        md9
      >
        <v-layout
          row
          wrap
        >
          <v-flex
            xs12
            d-flex
            v-for="(post, index) in posts.items"
            :key=index
          >
            <v-hover>
              <v-card
                slot-scope="{ hover }"
                :class="`elevation-${hover ? 12 : 2}`"
                class="mx-auto"
                width="600"
              >
                <v-img
                  :src="require('@/assets/vuejs-flask-spa.jpg')"
                  aspect-ratio="2.75"
                ></v-img>

                <!-- <div style="margin-top: -24px; margin-left: 16px;">
                  <v-avatar>
                    <img
                      :src="post.author._links.gravatar"
                      alt="author"
                      style="border: solid 1px transparent !important; border-color: #fff !important; border-width: 2px !important;"
                    >
                  </v-avatar>
                  <div class="mt-2">
                    <v-tooltip left>
                      <template v-slot:activator="{ on }">
                        <a
                          class="subheading green--text"
                          v-on="on"
                          href="#/about"
                        >{{ post.author.name }}</a>
                      </template>
                      <span>作者</span>
                    </v-tooltip>
                    <span class="grey--text pl-2">{{ $moment(post.timestamp).fromNow() }}</span>
                  </div>
                </div> -->

                <v-avatar style="margin-top: -24px; margin-left: 8px;">
                  <img
                    :src="post.author._links.gravatar"
                    alt="author"
                    style="border: solid 1px transparent !important; border-color: #fff !important; border-width: 2px !important;"
                  >
                </v-avatar>

                <div class="px-3 py-1">
                  <v-tooltip left>
                    <template v-slot:activator="{ on }">
                      <a
                        class="subheading green--text"
                        v-on="on"
                        href="#/about"
                      >{{ post.author.name }}</a>
                    </template>
                    <span>作者</span>
                  </v-tooltip>
                  <span class="grey--text pl-2">{{ $moment(post.timestamp).fromNow() }}</span>
                </div>

                <v-card-title class="px-3 py-1">
                  <router-link
                    class="headline mb-0 postlink"
                    :to="{ name: 'post', params: { id: post.id } }"
                  >
                    {{ post.title }}
                  </router-link>
                </v-card-title>

                <v-card-text class="subheading px-3 py-1">
                  {{ post.summary }}
                </v-card-text>

                <v-card-actions class="px-3 py-1">
                  <v-icon color="grey">far fa-eye</v-icon>
                  <span class="pl-1 grey--text">{{ post.view }}</span>
                  <v-spacer></v-spacer>
                  <v-btn flat color="orange" :to="{ name: 'post', params: { id: post.id } }">阅读全文</v-btn>
                  <v-btn flat color="orange" :to="{ name: 'post', params: { id: post.id } }">编辑</v-btn>
                  <v-btn flat color="orange" @click="handleDelete(post.id)">删除</v-btn>
                </v-card-actions>

              </v-card>
            </v-hover>
          </v-flex>

        </v-layout>
      </v-flex>

      <Sidebar />

      <v-flex
        xs6
        pl-0
      >
        <v-pagination
          v-model="posts._meta.page"
          :length="posts._meta.total_pages"
          @input="pageRedirect"
        ></v-pagination>
      </v-flex>

    </v-layout>
  </v-container>
</template>

<script>
export default {
  name: 'Home',
  components: {
    Sidebar: () => import("@/components/Sidebar")
  },
  data: () => {
    return {
      posts: {
        _meta: {
          page: null,
          total_pages: null
        }
      }
    }
  },
  methods: {
    getPosts() {
      let page = 1
      let per_page = 10
      if (typeof this.$route.query.page !== 'undefined') {
        page = this.$route.query.page
      }
      if (typeof this.$route.query.per_page !== 'undefined') {
        per_page = this.$route.query.per_page
      }
      const path = `/posts?page=${page}&per_page=${per_page}`
      this.$axios
        .get(path)
        .then(response => {
          // handle success
          this.posts = response.data
        })
        .catch(error => {
          // handle error
          console.log(error.response.data)
        })
    },
    handleDelete(id) {
      const path = `/posts/${id}`
      this.$axios.delete(path).then(response => {
        console.log('success')
      }).catch(error => {
        console.log(error)
      })
    },
    pageRedirect(page) {
      this.$router.push({ name: 'home', query: { page: page } })
    }
  },
  created() {
    this.getPosts()
  },
  // 当查询参数 page 或 per_page 变化后重新加载数据
  beforeRouteUpdate(to, from, next) {
    console.log('Home RouterUpdate')
    next()
    this.getPosts()
  }
}
</script>