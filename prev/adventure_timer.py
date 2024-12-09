package main

import (
	"fmt"
	"net/http"
	"os"
	"strconv"
	"strings"
	"time"

	"github.com/gin-gonic/gin"
)

// 定义音乐播放函数 (此处仅做占位，实际需要整合音频播放库)
func playMusic(musicName string) {
	fmt.Println("Playing:", musicName)
}

// 倒计时函数
func countdown(h, m, s int) {
	totalSeconds := h*3600 + m*60 + s
	for totalSeconds > 0 {
		timer := fmt.Sprintf("%02d:%02d:%02d", totalSeconds/3600, (totalSeconds%3600)/60, totalSeconds%60)
		fmt.Printf("\r%s", timer)
		time.Sleep(1 * time.Second)
		totalSeconds--
	}
	fmt.Println()
}

// 带音乐播放的倒计时
func countdownWithPlayMusic(h, m, s int, musicName string) {
	countdown(h, m, s)
	playMusic(musicName)
}

// 定义主逻辑
func timeLoop(c *gin.Context, h1, m1, s1, h2, m2, s2, totalH, totalM, totalS int) {
	totalInputTime := totalH*3600 + totalM*60 + totalS
	timeDuration := h1*3600 + m1*60 + s1 + h2*3600 + m2*60 + s2
	num := totalInputTime / timeDuration

	for i := 1; i <= num; i++ {
		countdownWithPlayMusic(h1, m1, s1, "MusicNameForClassEnds")
		if i < num {
			countdownWithPlayMusic(h2, m2, s2, "MusicNameForClassBegins")
		}
	}

	c.JSON(http.StatusOK, gin.H{
		"message": fmt.Sprintf("Adventure ends. You defeated %d enemies!", num),
	})
}

// 启动 Gin Web 应用程序
func main() {
	r := gin.Default()

	r.POST("/start", func(c *gin.Context) {
		totalTime := c.PostForm("total_time")
		mode := c.PostForm("mode")

		// 解析输入的总时间
		times := strings.Split(totalTime, " ")
		if len(times) != 3 {
			c.JSON(http.StatusBadRequest, gin.H{"error": "Invalid time format. Use 'hh mm ss'"})
			return
		}

		totalH, _ := strconv.Atoi(times[0])
		totalM, _ := strconv.Atoi(times[1])
		totalS, _ := strconv.Atoi(times[2])

		// 解析模式
		switch mode {
		case "1": // Day mode: 40m + 10m
			timeLoop(c, 0, 40, 0, 0, 10, 0, totalH, totalM, totalS)
		case "2": // Night mode: 1h20m + 15m
			timeLoop(c, 1, 20, 0, 0, 15, 0, totalH, totalM, totalS)
		case "3": // 自定义模式
			lessonTime := c.PostForm("lesson_time")
			breakTime := c.PostForm("break_time")

			lesson := strings.Split(lessonTime, " ")
			breakT := strings.Split(breakTime, " ")
			if len(lesson) != 3 || len(breakT) != 3 {
				c.JSON(http.StatusBadRequest, gin.H{"error": "Invalid lesson or break time format. Use 'hh mm ss'"})
				return
			}

			h1, _ := strconv.Atoi(lesson[0])
			m1, _ := strconv.Atoi(lesson[1])
			s1, _ := strconv.Atoi(lesson[2])

			h2, _ := strconv.Atoi(breakT[0])
			m2, _ := strconv.Atoi(breakT[1])
			s2, _ := strconv.Atoi(breakT[2])

			timeLoop(c, h1, m1, s1, h2, m2, s2, totalH, totalM, totalS)
		default:
			c.JSON(http.StatusBadRequest, gin.H{"error": "Invalid mode. Choose 1, 2, or 3"})
		}
	})

	// 启动服务器
	port := os.Getenv("PORT")
	if port == "" {
		port = "8080"
	}
	r.Run(":" + port)
}