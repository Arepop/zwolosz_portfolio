import gql from "graphql-tag"

export const TILE_LIST_QUERY = gql`
            query {
                allTiles {
                  edges {
                    node {
                      name
                      fileName
                      created
                    }
                  }
                }
              }
              `