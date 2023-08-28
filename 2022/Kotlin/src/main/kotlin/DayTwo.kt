import java.io.File

// A, X - rock    [1]
// B, Y - paper   [2]
// C, Z - scissor [3]
// loss           [0]
// draw           [3]
// win            [6]
fun main(){
    var score = 0
    File("./inputs/2-full.txt").forEachLine {
        val (a, b) = Pair(it.substringBefore(" "), it.substringAfter(" "))
        when (a) {
            "A" -> {
                when (b) {
                    "X" -> { score += 4 }
                    "Y" -> { score += 8 }
                    "Z" -> { score += 3 }
                }
            }
            "B" -> {
                when (b) {
                    "Y" -> { score += 5 }
                    "Z" -> { score += 9 }
                    "X" -> { score += 1 }
                }
            }
            "C" -> {
                when (b) {
                    "Z" -> { score += 6 }
                    "X" -> { score += 7 }
                    "Y" -> { score += 2 }
                }
            }
        }
    }
    println(score)
}