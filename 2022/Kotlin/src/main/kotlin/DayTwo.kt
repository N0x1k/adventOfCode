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
        when {
            it.contains("X") -> score += 1
            it.contains("Y") -> score += 2
            it.contains("Z") -> score += 3
        }
        when {
            it.contains(Regex("A X|B Y|C Z")) -> score += 3
            it.contains(Regex("A Y|B Z|C X")) -> score += 6
        }
    }
    println(score)
}