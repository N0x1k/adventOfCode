import java.io.File

fun partOne(inputFile: String): MutableList<Int> {
    var sum = 0
    val results: MutableList<Int> = mutableListOf()

    File(inputFile).forEachLine {
        if (it.isNotBlank()) {
            sum += it.toInt()
        } else {
            results.add(sum)
            sum = 0
        }
    }
    return results
}

fun main() {
    val resultsOne: MutableList<Int> = partOne("./inputs/1-full.txt")
    println(resultsOne.max())
    // part two
    println(resultsOne.sortedDescending().subList(0,3).sum())
}
